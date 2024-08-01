import React from 'react';

const MangaCard = ({ Manga }) => {
    return (
        <div className = "Manga">
            <div>
                <p> {Manga.} </p>
            </div>
            
            <div>
                <img src = {Manga.Poster !== 'N/A' ? Manga.Poster : 'https://via.placeholder.com/400'} alt = "Manga poster" />
            </div>

            <div>
                <span> {Manga.Type} </span>
                <h3>{Manga.Title}</h3>
            </div>
        </div>
    )
}

export default MangaCard;