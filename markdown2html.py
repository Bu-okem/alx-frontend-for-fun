#!/usr/bin/python3
"""
converts a markdown file to HTML.
"""

import argparse
import pathlib
import re


def convert_md_to_html(input_file, output_file):
    '''
    converts markdown file to HTML file
    '''
    # read the contents of the input file
    with open(input_file, encoding='utf-8') as f:
        md_content = f.readlines()

    html_content = []
    for line in md_content:
        # check if the line is heading
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            # get the level of the heading
            h_level = len(match.group(1))
            # get the content of the heading
            h_content = match.group(2)
            # append the html equivalent of the heading
            html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_content.append(line)

    # write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    # check if input file exists
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # convert markdown file to html
    convert_md_to_html(args.input_file, args.output_file)


