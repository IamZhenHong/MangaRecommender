import React from 'react';

const MangaCard = ({ manga }) => {
    return (
        <div className = "manga">
            <div>
                <p> {manga.score} </p>
            </div>
            
            <div>
                <img src = {manga.image_url !== 'N/A' ? manga.image_url : 'https://via.placeholder.com/400'} alt = "Manga poster" />
            </div>

            <div>
                <span> {manga.Type} </span>
                <h3>
                    <a href={manga.url} target="_blank" rel="noreferrer noopener">
                        {manga.title}
                    </a>
                </h3>
            </div>
        </div>
    )
}

export default MangaCard;