const fs = require('fs')

function add_book() {
    book_name = document.getElementById("bname").value;
    book_author = document.getElementById("bauthor").value;
    book_desc = document.getElementById("bdesc").value;
    book_page = document.getElementById("bpage").value;
    book_hardback = document.getElementById("bhardback").value;
    book_paperback = document.getElementById("bpaperback").value;
    book_total = document.getElementById("btotal").value;
}