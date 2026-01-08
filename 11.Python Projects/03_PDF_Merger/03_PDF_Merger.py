from pathlib import Path
from PyPDF2 import PdfWriter

BASE_DIR = Path(__file__).parent  # folder where script lives

def main():
    writer = PdfWriter()

    n = int(input("How many PDFs do you want to merge? "))

    pdf_paths = []
    for i in range(n):
        name = input(f"Enter the name of PDF {i+1}: ").strip()
        p = BASE_DIR / name
        if not p.exists():
            print(f"File not found in {BASE_DIR}: {name}")
            return
        pdf_paths.append(p)

    for p in pdf_paths:
        writer.append(str(p))
        print(f"Successfully Added: {p.name}")

    out_name = input("Enter name for merged PDF without .pdf: ").strip() or "merged"
    out_path = BASE_DIR / f"{out_name}.pdf"

    with open(out_path, "wb") as f:
        writer.write(f)
    writer.close()

    print(f"Done! Saved as: {out_path.resolve()}")

if __name__ == "__main__":
    main()
