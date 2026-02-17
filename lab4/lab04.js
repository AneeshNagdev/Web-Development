function bookmarksChecker(){
    let websites = [
        "https://www.google.com",
        "https://www.netflix.com",
        "http://www.example.com",
        "http://www.aneesh.com"
    ];

    let bookmarksDiv = document.getElementById('bookmarks');

    for (let i = 0; i < websites.length; i++){
        let url = websites[i];
        let icon = "";

        if (url.startsWith("https")){
            icon = "🔒"
        }else{
            icon = "🔓"
        }

        bookmarksDiv.innerHTML += icon + " <a href='#'>" + url + "</a><br>";
    }

    
}

profsStrings = [
    "Mr. Owl ate my metal worm.",
    "I’m on a seafood diet. I see food and I eat it.",
    "level",
    "Love is sharing your popcorn.",
    "Was it a car or a cat I saw?",
    "racecar",
    "no lemon, no melon",
    "A man, A plan, A canal - Panama!"
]

//keeping only the letters in the string.
function lettersOnly(str){
    let newString = "";
    str = str.toLowerCase();

    for(let i = 0; i < str.length; i++){
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= '0' && str[i] <= '9')){
            newString += str[i]
        }

    }

    return newString;
}

function palindromeChecker(str){
    let checkingStr = lettersOnly(str);
    let reversedString = checkingStr.split("").reverse().join("");

    if (checkingStr === reversedString) {
        return true;
    }else{
        return false;
    }


}

function testingProfsString(){

    let resultsDiv = document.getElementById('profsStrings');

    for (let i = 0; i < profsStrings.length; i++){

        if (palindromeChecker(profsStrings[i]) == true ) {
            resultsDiv.innerHTML += "<p style='color: #8a2086; text-decoration: none; font-size: 18px;'> The String is palindrome: "+ profsStrings[i] + "</p>";

        }else{
            resultsDiv.innerHTML += "<p style='color: #4573b0; text-decoration: underline; font-size: 18px;'>The String is not palindrome: "+ profsStrings[i] + "</p>";

        }
    }
}

function showingResult(){
    let str = document.getElementById('textBox').value;
    let result = document.getElementById('result');
    let txt = document.getElementById('result2');

    if (palindromeChecker(str)){
        result.innerHTML = "The string is Palindrome";
        txt.innerHTML = str;
        txt.style.color = '#8a2086';
        txt.style.textDecoration = 'none';
        txt.style.fontSize = '18px';
    }else{
        result.innerHTML = "The string is not Palindrome";
        txt.innerHTML = str;
        txt.style.color = '#4573b0';
        txt.style.textDecoration = 'underline';
        txt.style.fontSize = '18px';
    }
}

bookmarksChecker();
testingProfsString();