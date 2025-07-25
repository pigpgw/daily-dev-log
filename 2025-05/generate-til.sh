#!/bin/bash

start_date="2025-07-25"
end_date="2025-08-31"
template_file="template.md"

current_date="$start_date"

while [[ "$current_date" < "$end_date" || "$current_date" == "$end_date" ]]; do
  year=$(date -j -f "%Y-%m-%d" "$current_date" "+%Y")
  month=$(date -j -f "%Y-%m-%d" "$current_date" "+%m")
  day=$(date -j -f "%Y-%m-%d" "$current_date" "+%d")

  folder="2025-$month"
  filename="$folder/2025-$month.$day.md"

  mkdir -p "$folder"
  cp "$template_file" "$filename"

  echo "✅ Created $filename"

  current_date=$(date -j -v+1d -f "%Y-%m-%d" "$current_date" "+%Y-%m-%d")
done

