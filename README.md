# StaticSiteGenerator

A lightweight static site generator written in Python that converts Markdown files into a fully-rendered HTML website. This project was created as part of the Boot.dev *“Build a Static Site Generator”* course.

## Features

* Converts Markdown (`.md`) files to HTML
* Uses HTML templates for consistent page layout
* Generates a complete static website from the `content/` directory
* Builds automatically into the `public/` output folder
* Copies CSS and other static assets
* Supports navigation between generated pages
* Simple structure that’s easy to extend

## How It Works

1. Add Markdown files to the `content/` directory.
2. The generator reads and parses each Markdown file.
3. Templates from the `templates/` folder are applied.
4. HTML files are written into the `public/` directory.
5. Static assets are copied into the output folder.
6. The site is ready to open locally or deploy to any static host.

## Project Structure

```
.
├── content/        # Source Markdown files
├── templates/      # Base HTML templates
├── static/         # CSS, images, and other static assets
├── docs/           # Generated HTML site(ouput)
├── main.py         # Build script/entry point
└── README.md
```


## Requirements

* Python 3.10+
* Optional: dependencies listed in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the generator from the project root:

```bash
python main.py
```

The build process will:

* Read Markdown files from `content/`
* Convert them into HTML using `templates/`
* Output the final site to `docs/`
* Copy assets (CSS, images, etc.)

When done, open:

```
docs/index.html
```

to view your generated site.

## Customization

* **Styling:** Edit `static/styles.css` to change the visual design.
* **Templates:** Modify HTML files in `templates/` to update layout, header, footer, etc.
* **Add Pages:** Create more `.md` files in `content/` to automatically generate new pages.

## Future Improvements

Some ideas to extend the project:

* Blog posts with metadata (dates, tags, slugs)
* Automatic index or blog listing pages
* Syntax highlighting for code blocks
* Pagination
* RSS or Atom feed generation
* Pretty URLs / routing system
