import os
from docx import Document
from pdf2image import convert_from_path

INPUT_DIR = "docs"
OUTPUT_DIR = "converted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_docx_to_html(input_path, output_path):
    doc = Document(input_path)
    html = "<html><body>"

    for p in doc.paragraphs:
        html += f"<p>{p.text}</p>"

    # extract images
    for rel in doc.part._rels:
        rel = doc.part._rels[rel]
        if "image" in rel.target_ref:
            img_name = os.path.basename(rel.target_ref)
            img_path = os.path.join(OUTPUT_DIR, img_name)

            with open(img_path, "wb") as f:
                f.write(rel.target_part.blob)

            html += f'<img src="{img_name}" style="max-width:100%; margin-top:10px;">'

    html += "</body></html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def convert_pdf_to_html(input_path, output_path):
    images = convert_from_path(input_path)
    html = "<html><body>"

    for i, img in enumerate(images):
        img_name = f"{os.path.basename(input_path)}_{i}.png"
        img_path = os.path.join(OUTPUT_DIR, img_name)
        img.save(img_path, "PNG")

        html += f'<img src="{img_name}" style="max-width:100%; margin-top:10px;">'

    html += "</body></html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


week_files = {
    1: "Java-week-1.docx",
    2: "Java-week-2.docx",
    3: "Java-week-3.docx",
    4: "Java week-4.docx",
    5: "Java week-5.docx",
    6: "JAVA-WEEK-6.docx",
    7: "Java-week-7.docx",
    8: "JAVA-WEEK-8.docx",
    9: "JAVA-WEEK-9.docx",
    10: "JAVA-WEEK-10.docx",
    11: "JAVA-WEEK-11.docx",
    12: "JAVA-WEEK-12.docx",
}

for week, filename in week_files.items():
    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, f"week{week}.html")

    print(f"Converting Week {week}: {filename}")

    if filename.lower().endswith(".pdf"):
        convert_pdf_to_html(input_path, output_path)
    else:
        convert_docx_to_html(input_path, output_path)

print("✔ Conversion complete! Check the 'converted/' folder.")
