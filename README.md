# Movies Trailer Project
 
 This project creates a html file called **"fresh_tomatoes"** that displays top rated movies' poster and plays a trailer when clicked.

## Prerequisites

To run this program you will require the following installed on your system:
1- Python 2.7 
2- Web browser e.g. Chrome, Firefox	

## Files 

- **fresh_tomatoes.py** - Contains open_movies_page function that generate web page from a list of movies.

- **media.py** - Defines the "Movie" class, includes constructor and show_trailer function that shows the trailer for a movie in a new window.

- **entertainment_center.py** - Main module to retreive data through api and generate movies list and parse data to open_movies_page function for web page creation.

## How to run

1- Place all files into a common directory.

2- Double click **entertainment_center.py** and python.exe window should appear and compile the program.

3- Program will open the webpage displaying the movies list and "fresh_tomatoes.html" file would be created in the same directory.

## License

MIT License

Copyright (c) 2018 Wong See Lai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Credits

This product uses the [TMDb API](https://www.themoviedb.org/) but is not endorsed or certified by TMDb.
