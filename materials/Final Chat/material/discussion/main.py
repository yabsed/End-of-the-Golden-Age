import pathlib

def merge_markdown_files(output_filename="merged_all.md"):
    # 현재 작업 디렉토리 설정
    current_dir = pathlib.Path.cwd()
    
    # 출력 파일 경로 설정
    output_path = current_dir / output_filename
    
    # 디렉토리 내 모든 .md 파일 찾기 (출력 파일 제외)
    md_files = sorted([
        f for f in current_dir.glob("*.md") 
        if f.name != output_filename
    ])

    if not md_files:
        print("합칠 마크다운 파일이 없습니다.")
        return

    with open(output_path, "w", encoding="utf-8") as outfile:
        for i, file_path in enumerate(md_files):
            with open(file_path, "r", encoding="utf-8") as infile:
                # 파일 간 구분을 위해 파일명을 헤더로 추가 (선택 사항)
                outfile.write(f"\n\n---")
                outfile.write(f"\n## 파일 출처: {file_path.name}\n\n")
                
                # 내용 작성
                outfile.write(infile.read())
                
                # 파일 끝에 줄바꿈 추가 (내용이 붙는 것 방지)
                outfile.write("\n")
                
            print(f"[{i+1}/{len(md_files)}] {file_path.name} 합치기 완료")

    print(f"\n✅ 모든 파일이 '{output_filename}'으로 합쳐졌습니다.")

if __name__ == "__main__":
    merge_markdown_files()