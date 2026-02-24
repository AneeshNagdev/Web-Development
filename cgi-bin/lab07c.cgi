#!/usr/bin/perl -T
use CGI ':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
use File::Basename; 

print "Content-type: text/html\n\n";

my $safe_filename_characters = "a-zA-Z0-9_.-";

my $upload_dir = "../lab7";

my $query = new CGI;

my $filename = $query->param("imagefile");

my $text = param('usertext');

if (!$filename) {
    
    print "<h2>There was a problem uploading your picture.</h2>";
    exit;
}

my ($name, $path, $extension) = fileparse($filename, '\..*');

$filename = $name . $extension;

$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;

if ($filename =~ /^([$safe_filename_characters]+)$/) {
    $filename = $1;  
} else {
    die "Filename contains invalid characters";
}

my $upload_filehandle = $query->upload("imagefile");

open (UPLOADFILE, ">$upload_dir/$filename") or die "$!";
binmode UPLOADFILE;

while (<$upload_filehandle>) {
    print UPLOADFILE ;
}

close UPLOADFILE;

print qq{
    <!DOCTYPE html>
    <html>
        <head>
            <title>Upload Result</title>

            <style>
                body {
                    font-family: Arial; 
                    background-color: #faf4d2;
                }
                .box {
                    width: 600px;
                    margin: 40px auto;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    border: 1px solid #ccc;
                    text-align: center;
                    box-shadow: 3px 3px 7px rgba(0,0,0,0.4);
                }
                img {
                    max-width: 90%;
                    border: 1px solid #999;
                    margin-top: 10px;
                }

                p {
                    font-size: 20px;
                    color: #333333;
                    margin: 15px 0;
                    font-weight: 200;
                }
            
            </style>
        
        </head>

        <body>
            <div class="box">
                <h2>Here is your uploaded image:</h2>
                <img src="../lab7/$filename" alt="Uploaded Image">

                <h3>Your Text:</h3>
                <p>$text</p>
            </div>
        </body>
    
    </html>

};