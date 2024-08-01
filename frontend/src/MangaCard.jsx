import React from 'react';

const MangaCard = ({ Manga }) => {
    return (
        <div className = "Manga">
            
            
            <div>
                <img src = {Manga.image_url !== 'N/A' ? Manga.image_url : 'https://via.placeholder.com/400'} alt = "Manga poster" />
            </div>

            <div>
                <span> {Manga.Type} </span>
                <h3>{Manga.title}</h3>
            </div>
        </div>
    )
}

export default MangaCard;