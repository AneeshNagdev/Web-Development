#!/usr/bin/perl -T
print "Content-type: text/html\n\n";

print qq{
    <!DOCTYPE html>
    <html lang='en'>
        <head>
            <link href="https://fonts.googleapis.com/css2?family=Roboto&family=Merriweather&display=swap" rel="stylesheet">
            <title>My First Perl Program</title>

            <style>
                h1 {
                    font-family: 'Roboto', sans-serif;
                    font-size: 50px;
                    color: blue;
                    text-align: center;
                    margin-top: 60px;
                }
                body{
                    background-color: #e0dedeff;
                }
            </style>

        </head>
        <body>
            <h1>This is my first Perl program</h1>
        </body>
    </html>
}