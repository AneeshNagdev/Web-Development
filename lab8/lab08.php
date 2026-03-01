<?php
    $lastTime = time() + (48*60*60);

    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["favImage"])) {
        $fav = $_POST["favImage"];
        setcookie("favImage", $fav, $lastTime);
        $_COOKIE["favImage"] = $fav;
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab 08</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            background: url('https://ihypress.de/textureland/n031.jpg');
            color: white;
            font-size: 25px;
            background-size: cover;
        }

        .background h1 {
            padding: 50px 20px;
            margin: 0;
            text-align: center;
            color: white;
        }

        .background {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 120px;
            text-align: center;
        }

        table {
            border-collapse: collapse;
            width: 80%;
            margin-top: 20px; 
            margin-left: 20px;
            background: url('https://i.imgur.com/Gl6idc4.jpg') repeat;
        }

        table td {
            padding: 15px;
            border: 2px solid #fff;
            color: white;
            text-align: center;
            font-size: 24px;
        }

        .image-section {
            margin-top: 40px;
            text-align: center;
        }

        .image-grid {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 15px;
        }

        .image-grid img{
            width: 150px;
            border: 3px solid white;
            border-radius: 5px;
        }

        .image-grid img:hover {
            cursor: pointer;
        }

        .fav-box {
            margin-top: 30px;
            text-align: center;
        }

        .fav-box img{
            max-width: 60%;
            height: 70%;
            border: 3px solid red;
            border-radius: 10px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <?php
    $hour = date("H");
    $greeting = "";
    $textColor = "";

    if ($hour >= 6 && $hour < 12) {
        $bg = "https://ihypress.de/textureland/n024.jpg";
        $greeting = "Good Morning!";
        $textColor = "#000";
    } elseif ($hour >= 12 && $hour < 17) {
        $bg = "https://ihypress.de/textures/anim_yellow.gif";
        $greeting = "Good Afternoon!";
        $textColor = "#000";
    } elseif ($hour >= 17 && $hour < 21) {
        $bg = "https://ihypress.de/textures/falling_snow.gif";
        $greeting = "Good Evening!";
        $textColor = "#fff";
    } else {
        $bg = "https://ihypress.de/textures/night_sky.gif";
        $greeting = "Good Night!";
        $textColor = "#fff";
    }
    
    echo "<div class='background' style='background: url($bg); background-size: cover;'> <h1 style='color: $textColor;'>$greeting</h1></div>";
    ?>

    <div class="form-section">
        <h2>Multiplication Table</h2>
        <form action="https://www.cs.torontomu.ca/~anagdev/lab8/lab08.php" method="post">
            <label for="rows">Number of Rows (3-12):</label>
            <input type="number" name="rows" id="rows" required >
            <label for="columns">Number of Columns (3-12)</label>
            <input type="number" name="cols" id="cols" required>
            <button type="submit">Generate Table</button>
        </form>
    </div>
    
    <?php
    

    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['rows']) && isset($_POST['cols'])) {
        $rows = (int)($_POST["rows"]);
        $cols = (int)($_POST['cols']);

        if (($rows < 3) || ($rows > 12) || ($cols < 3) || ($cols > 12)) {
            echo "<p style='color: red;'>Invalid Input. Please make sure the input is between 3 and 12.</p>";
        } else {
            echo "<div class='form-section'><table>";
                for ($i = 1; $i <= $rows; $i++) {
                    echo "<tr>";
                    for ($j = 1; $j <= $cols; $j++) {
                        echo "<td>" . ($i * $j) . "</td>";

                    }
                    echo "</tr>";
                }
                echo "</table></div>";
        }
    }
    ?>

    <div class="image-section">
        <h2>Pick Your Favorite Image</h2>
        <form action="https://www.cs.torontomu.ca/~anagdev/lab8/lab08.php" method="post">
            <div class="image-grid">
                <label >
                    <input type="radio" name="favImage" value="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=02" required>
                    <img src="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=02" alt="Image 1">
                </label>
                <label >
                    <input type="radio" name="favImage" value="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=09" required>
                    <img src="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=09" alt="Image 2">
                </label>
                <label >
                    <input type="radio" name="favImage" value="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=18" required>
                    <img src="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=18" alt="Image 3">
                </label>
                <label >
                    <input type="radio" name="favImage" value="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=25" required>
                    <img src="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=25" alt="Image 4">
                </label>
                <label >
                    <input type="radio" name="favImage" value="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=51" required>
                    <img src="https://ihypress.de/wallpapers/astronomy/wallpaper.php?image=51" alt="Image 5">
                </label>
                </div>
                <button type="submit" style="margin-top: 10px;">Save</button>
        </form>
    </div>

    <?php
    if (!isset($_COOKIE["favImage"])) {
        echo "<p>Welcome! Please choose your favourite image below.</p>";

    } else {
        echo "<div class='fav-box'>";
        echo "<h2>Your Favourite Image</h2>";
        echo "<img src='" . $_COOKIE["favImage"] . "'>";
        echo "</div>";
    }
    ?>
</body>
</html>
