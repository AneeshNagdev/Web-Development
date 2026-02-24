#!/usr/bin/perl -T
use CGI ':standard';
print "Content-type: text/html\n\n";

my $fname = param('fname');
my $lname = param('lname');
my $street = param('street');
my $city = param('city');
my $postal = param('postal');
my $province = param('province');
my $phone = param('phone');
my $email = param('email');
my $payment = param('payment');

my @errors = ();

if ($phone !~ /^[0-9]{10}$/) {
    push @errors, "Phone number must be 10 digits.";
}

if ($postal !~ /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/) {
    push @errors, "Postal code must be in 'L0L 0L0' format.";
}

if ($email !~ /^[A-Za-z0-9._%+-]+\@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$/) {
    push @errors, "Invalid email address format.";
}

if ($fname eq "") {
    push @errors, "Can't leave first name empty";
}
if ($lname eq "") {
    push @errors, "Can't leave last name empty";
}
if ($street eq "") {
    push @errors, "Street address is required. Please fill it out";
}
if ($city eq "") {
    push @errors, "You much provide your city name";
}
if ($province eq "") {
    push @errors, "Please select one province";
}
if ($payment eq "") {
    push @errors, "Payment type is required. Please select one";
}

if (@errors > 0) {
    print "<html><head><title>Errors Found</title>";

    print << "STYLE";

<style>
body { font-family: Arial; background-color: #f4f4f4; }
.errbox {
    width: 500px; margin: 40px auto; background: white; padding: 20px; border-radius: 8px; border: 1px solid red
}
li { color: red; margin: 8px 0; padding: 10px; border-radius: 6px; border: 1px solid #ff6b6b; font-weight: bold; }
#Rbutton { display: inline-block; margin: 20px auto 0; text-align: center; background-color: #ff6b6b; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; }

</style>
STYLE

    print "</head><body>";

    print "<div class='errbox'>";
    print "<h2>There were errors in your submission:</h2>";
    print "<ul>";

    foreach my $e (@errors) {
        print "<li>$e</li>";
    }

    print "</ul>";
    print "<a href='../lab7/lab07b.html' id='Rbutton'>Return to form</a>";
    print "</div></body></html>";

    exit;
}

print "<html><head><title>Reservatoin Summary</title>";

print << "STYLE";
<style>
body { font-family: Arial; background-color: #e8d8885f; }
.box {
    width: 600px; margin: 40px auto; background: rgba(237,215,150,0.9);
    padding: 20px; border-radius: 8px; border: 1px solid #ccc;
}
h2 { text-align: center; }
</style>
STYLE

print "</head><body>";

print "<div class='box'>";
print "<h2>Reservation Details</h2>";

print "<p><b>First Name:</b> $fname</p>";
print "<p><b>Last Name:</b> $lname</p>";
print "<p><b>Street Address:</b> $street</p>";
print "<p><b>City:</b> $city</p>";
print "<p><b>Postal Code:</b> $postal</p>";
print "<p><b>Province:</b> $province</p>";
print "<p><b>Phone:</b> $phone</p>";
print "<p><b>Email:</b> $email</p>";
print "<p><b>Payment Method:</b> $payment</p>";

print "</div></body></html>";
