# SIRPAS

Simple Role Play Adventure System. 

SIRPAS is meant to be a complete and detailed RPG system you can pick up
to play adventures in any fantasy (or real) world you can imagine, and can be
set up in one minute for a 2 hours night of fun with friends, or become a deep and
intriguing hobby with unparalleled depth.

## How-to

Books illustrating the systems are under the Books/ directory; they are broken down
in multiple Markdown files, for simpler editing and re-organization.

The file called `main.md` contains the top-level
inclusion directives to create the final assembled markdown.

1. Use `Scripts/build.py Source/<Book_you_want>/main.md -o <target.md>` to assemble a
markdown file.
1. Use your favorite .md renderer to create your final product. We suggest iconv/pandoc.

# Contributing

It's the usual thing; create a fork and file a pull request, or file a issue in the github 
**issues** section.

## Creating an extension

Sirpas extensions, also called *settings*, have a master document in the root directory of the
repository, which includes the documents in a sub-directory with their own same name though
the include directive. See the London Mysteries setting for an example.

## Cross-linking

You can cross-link existing headers by using the Markdown format, `[text to link](#target-header-id)`

## Special Commands

TODO

# License

[![Creative Commons License BY-NC-SA](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

SIRPAS and all the IP in the SIRPAS project are licensed under 
Creative Commons, Attribution, Non-Commercial, Share-alike.

(C) Giancarlo Niccolai, 2018
