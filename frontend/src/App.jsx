import react from "react"
import { useState,useEffect } from "react";
import searchIcon from './search.svg';
import MangaCard from './MangaCard';
import api from "./api";
import './App.css';
const App = () => {
  const [mangas, setMangas] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  const searchMangas = async (manga_title) => {
    try {
      const response = await api.get(`/api/get/?manga_title=${manga_title}`);
      const data = JSON.parse(response.data);

  
      setMangas(data);
    
    } catch (error) {
      console.error('Error fetching mangas:', error);
      // Handle the error appropriately (e.g., display a user-friendly message)
    }
  };
  
  useEffect(() => {  
      searchMangas('Berserk');
      
      }
  , []);


  return (
      <div className="app">
          <h1> MangaRecommender </h1>
          <input
            placeholder = "Search for a manga"
            value = {searchTerm}
            onChange = {(e) => setSearchTerm(e.target.value)}
          />
          <img 
              src ={searchIcon}
              alt = "search"
              onClick = {() => searchMangas(searchTerm)}
          />

          {
              mangas?.length > 0
              ? (
                  <div className = "container">
                      
                      { mangas.map((manga) => (
                          <MangaCard manga = {manga} />
                      ))}
                  </div>
              ) : (
                  <div className = "empty">
                      <h2> No manga found</h2>
                      <h3> Hi</h3>
                      
                  </div>
                  
              )
          }
          
      </div>
  );
  }

export default App;