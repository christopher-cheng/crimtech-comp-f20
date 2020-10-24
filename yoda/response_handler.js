// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
    // Your Code Here

    text = document.getElementById("textbox").value

    img_new = ""
    quote_new = ""
    if (text.includes("cute") || text.includes("baby")) {
        if (text.includes("dark") && text.includes("force"))
            img_new = "img/cute-dark.jpg"
        else if (text.includes("force"))
            img_new = "img/cute-force.jpg"
        else
            img_new = "img/cute-std.jpg"
        quote_new = "h" + "m".repeat(1 + 20 * Math.random())
    } else {
        if (text.includes("dark") && text.includes("force")) {
            img_new = "img/regular-dark.jpg"
            quote_new = dark_quotes[Math.floor(Math.random() * dark_quotes.length)]
        } else if (text.includes("force")) {
            img_new = "img/regular-force.jpg"
            quote_new = force_quotes[Math.floor(Math.random() * force_quotes.length)]
        } else {
            img_new = "img/regular-std.jpg"
            quote_new = std_quotes[Math.floor(Math.random() * std_quotes.length)]
        }
    }
    document.getElementById("yoda_image").setAttribute("src", img_new)
    document.getElementById("quote").innerHTML = quote_new

    document.getElementById("textbox").value = ""
}