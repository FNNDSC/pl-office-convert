# Excel and ODS Spreadsheet to CSV Converter

[![Version](https://img.shields.io/docker/v/fnndsc/pl-office-convert?sort=semver)](https://hub.docker.com/r/fnndsc/pl-office-convert)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-office-convert)](https://github.com/FNNDSC/pl-office-convert/blob/master/LICENSE)
[![Build](https://github.com/FNNDSC/pl-office-convert/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-office-convert/actions)

`pl-office-convert` is a _ChRIS ds_ plugin which converts Excel and OpenOffice spreadsheet file
formats (`*.{xls,xlsx,ods}`) to the plaintext comma-separated values (`*.csv`) format.

## Usage

In `pl-office-convert` version 0.0.1 there are no options.
Every file in `inputdir/` ending with `.ods`, `.xlsx`, or `.xls` gets processed and written to
`outputdir/` by the same filename but with its file extension replaced with `.csv`.
Every other file in `inputdir/` is simply duplicated to `outputdir/`.

WARNING: only the first sheet of every file is converted!

```shell
singularity exec docker://docker.io/fnndsc/pl-office-convert:0.0.1 office_convert incoming/ outgoing/
```

## Planned Features

This plugin will eventually be a generic office format converter, being able to convert both ways from
office file format to plaintext and vice versa. But for now it is a simple single-purpose program.
