sed -i 's,\[sourcecode language="\([a-z]*\)"\],{% codeblock lang:\1 %},' *.markdown
sed -i 's,\[sourcecode lang="\([a-z]*\)"\],{% codeblock lang:\1 %},' *.markdown
sed -i 's,\[/sourcecode\],{% endcodeblock %},' *.markdown
sed -i 's/^_ /_/' *.markdown
sed -i 's,http://agateau.files.wordpress.com,,g' *.markdown
sed -i 's,http://agateau.wordpress.com,,g' *.markdown
sed -i 's,<code>,,g' *.markdown
sed -i 's,</code>,,g' *.markdown

# Kill trailing white spaces
sed -i 's,[ 	]*$,,' *.markdown
# Delete duplicate, consecutive lines from a file
sed -i '$!N; /^\(.*\)\n\1$/!P; D' *.markdown
