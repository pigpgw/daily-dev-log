#!/usr/bin/env python3
"""
중복된 섹션을 제거하는 스크립트
- "일" 섹션 중복 제거
- "프로젝트 작업" 섹션 중복 제거
- "일상 / 기타" 섹션 중복 제거
"""

import os
import re
import sys
from pathlib import Path


def remove_duplicate_section(content: str, section_title: str) -> str:
    """중복된 섹션을 제거합니다. 첫 번째 섹션을 제거하고 두 번째 섹션만 남깁니다."""
    lines = content.split("\n")
    result = []
    i = 0
    found_first = False
    skip_until_next_section = False

    while i < len(lines):
        line = lines[i]

        # 섹션 헤더 찾기
        if line == f"## {section_title}":
            if not found_first:
                # 첫 번째 섹션 발견 - 건너뛰기 시작
                found_first = True
                skip_until_next_section = True
                i += 1
                continue
            else:
                # 두 번째 섹션 발견 - 이제부터는 포함
                skip_until_next_section = False
                result.append(line)
                i += 1
                # 두 번째 섹션의 내용도 계속 포함
                continue

        # 건너뛰는 중이면 다음 섹션이나 구분선을 만날 때까지 건너뛰기
        if skip_until_next_section:
            # 다음 섹션 헤더를 만나면
            if line.startswith("## "):
                skip_until_next_section = False
                # 다음 섹션이 중복 섹션이면 (두 번째 섹션)
                if line == f"## {section_title}":
                    result.append(line)
                    i += 1
                    continue
                else:
                    # 다른 섹션이면 포함
                    result.append(line)
                    i += 1
                    continue
            else:
                # 건너뛰는 중 (첫 번째 섹션의 내용)
                i += 1
                continue

        # 일반 라인 추가 (두 번째 섹션의 내용 또는 다른 섹션)
        result.append(line)
        i += 1

    return "\n".join(result)


def fix_file(file_path: Path):
    """파일의 중복 섹션을 제거합니다."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # 각 섹션의 중복 제거
        content = remove_duplicate_section(content, "일")
        content = remove_duplicate_section(content, "프로젝트 작업")
        content = remove_duplicate_section(content, "일상 / 기타")

        # 내용이 변경되었으면 저장
        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"❌ 오류 발생 ({file_path}): {e}")
        return False


def main():
    target_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    print("🔍 중복 섹션 제거 시작...")
    print(f"📁 대상 경로: {target_path.absolute()}")

    # 파일인지 디렉토리인지 확인
    if target_path.is_file():
        md_files = [target_path]
    elif target_path.is_dir():
        md_files = list(target_path.rglob("*.md"))
    else:
        print(f"❌ 오류: {target_path}는 유효한 파일이나 디렉토리가 아닙니다.")
        sys.exit(1)

    # 날짜 및 요일 필터링 함수
    def get_date(file_path):
        name = file_path.name
        if "2026-01." in name or "2026-02." in name:
            try:
                parts = name.replace(".md", "").split(".")
                if len(parts) >= 2:
                    day = int(parts[1])
                    return day
            except:
                return 0
        return 0

    def is_weekday(file_path):
        """파일명에서 요일을 추출하여 평일인지 확인"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                first_line = f.readline()
                # 예: "# TIL | 2026.01.07 (수요일)"
                if "(" in first_line and ")" in first_line:
                    weekday = first_line.split("(")[1].split(")")[0]
                    # 주말 제외
                    if "토요일" in weekday or "일요일" in weekday:
                        return False
                    return True
        except:
            pass
        return True  # 확인 불가시 포함

    # 1월 7일 이후 평일 파일만 필터링
    filtered_files = []
    for f in md_files:
        if "2026-01" in str(f):
            day = get_date(f)
            if day >= 7 and is_weekday(f):
                filtered_files.append(f)
        elif "2026-02" in str(f):
            if is_weekday(f):
                filtered_files.append(f)

    md_files = sorted(filtered_files, key=lambda x: (str(x), get_date(x)))

    print(f"📄 발견된 마크다운 파일 (1월 7일 이후 평일): {len(md_files)}개")

    fixed_count = 0
    for md_file in md_files:
        if fix_file(md_file):
            fixed_count += 1
            print(f"✅ 수정됨: {md_file}")

    print(f"\n✅ 완료! {fixed_count}개 파일이 수정되었습니다.")


if __name__ == "__main__":
    main()
