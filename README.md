# NLP-Movie-Recommendations
This project allows users to type in a prompt describing the kind of movie they want to watch. In the prompt they can specify any of the following properties:
- Release Year (or range)
- Release Date (or range)
- Region where the film was produced or takes place
- Cast
- Production Companies
- Crew
- Genres
- Keywords
- Origin Country
- Original Language
- People (e.g. characters, actors)
- Runtime

The users can also specify the following properties they do not want the returned movies to have:
- Companies
- Genres
- Keywords 

The user prompt is run through a LLM to classify the parts of the prompt into the above categories. Then these are used to query The Movie Database API to return movies with similar properties.