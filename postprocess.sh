sed -i 's,\[sourcecode language="\([a-z]*\)"\],{% codeblock lang:\1 %},' *.markdown
sed -i 's,\[sourcecode lang="\([a-z]*\)"\],{% codeblock lang:\1 %},' *.markdown
sed -i 's,\[/sourcecode\],{% endcodeblock %},' *.markdown
sed -i 's/^_ /_/' *.markdown
sed -i 's,http://agateau.files.wordpress.com,,g' *.markdown
