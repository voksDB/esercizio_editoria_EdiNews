import yaml
import bibtexparser

def load_yaml_metadata(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_markdown_content(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_bib_entries(bib_path):
    with open(bib_path, "r", encoding="utf-8") as bibfile:
        return bibtexparser.load(bibfile).entries

def format_reference(entry):
    authors = entry.get("author", "Autore sconosciuto").replace(" and ", ", ")
    title = entry.get("title", "").strip("{}")
    journal = entry.get("journal", "")
    year = entry.get("year", "")
    doi = entry.get("doi", "")
    url = f"https://doi.org/{doi}" if doi else ""
    return f"- {authors} ({year}). *{title}*. {journal}. {url}"

def generate_references_section(bib_entries):
    refs = [format_reference(e) for e in bib_entries]
    return "## Riferimenti\n\n" + "\n".join(refs)

def generate_download_links():
    return (
        "#### Scarica il contenuto\n\n"
        "📄 [Scarica il PDF](https://voksdb.github.io/esercizio_editoria_EdiNews/downloads/clima_salute_mentale.pdf)  \n"
        "📝 [Scarica il Markdown](https://voksdb.github.io/esercizio_editoria_EdiNews/downloads/clima_salute_mentale.md)\n"
    )

def build_hugo_markdown(metadata, content, refs_section, download_links):
    # Estrai summary dal campo abstract
    summary_text = metadata.pop('abstract', '').strip()
    metadata['summary'] = summary_text

    # Inserisci la sezione introduttiva nel corpo (come primo paragrafo)
    intro = f"{summary_text}\n\n"
    content_with_intro = intro + content.strip()

    # Mantieni autore nel formato stringa
    if isinstance(metadata.get("author"), (list, tuple)):
        metadata["author"] = ", ".join(metadata["author"])

    # YAML front matter
    front_matter = "---\n" + yaml.dump(metadata, allow_unicode=True, sort_keys=False) + "---\n\n"

    # Corpo completo: front matter + contenuto + download + riferimenti
    body = (
        front_matter +
        content_with_intro +
        "\n\n---\n\n" +
        download_links +
        "\n\n---\n\n" +
        refs_section +
        "\n"
    )
    return body

def save_output(path, markdown):
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ Post Hugo pronto: {path}")

if __name__ == "__main__":
    meta = load_yaml_metadata("metadati.yaml")
    art = load_markdown_content("articolo_completo.md")
    bib_entries = load_bib_entries("bibliografia.bib")
    refs = generate_references_section(bib_entries)
    download = generate_download_links()
    result = build_hugo_markdown(meta, art, refs, download)
    save_output("clima_salute_mentale.md", result)
