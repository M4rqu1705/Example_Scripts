import React, { useState, useEffect } from 'react';
import PokeList from './PokeList'
import Pagination from './Pagination'
import axios from 'axios'
import "./style.scss"

const MAIN_API_URL = "https://pokeapi.co/api/v2/pokemon";

function App() {
  const [pokemon, setPokemon] = useState([]);
  const [currentPageURL, setCurrentPageURL] = useState(MAIN_API_URL);
  const [nextPageURL, setNextPageURL] = useState("");
  const [prevPageURL, setPrevPageURL] = useState("");
  const [loading, setLoading] = useState(true);


  useEffect(function () {
    setLoading(true);
    let cancel;

    axios.get(
      currentPageURL, {
      cancelToken: new axios.CancelToken(c => cancel = c)
    })
      .then(
        (res) => {
          setPokemon(res.data.results.map(p => p.name))
          setNextPageURL(res.data.next);
          setPrevPageURL(res.data.previous);
          setLoading(false);
        }
      );

    return () => cancel();


  }, [currentPageURL]);

  function gotoNextPage() {
    setCurrentPageURL(nextPageURL);
  }

  function gotoPrevPage() {
    setCurrentPageURL(prevPageURL);
  }

  if (loading) return <h1>Loading</h1>;

  return (
    <>
      <PokeList pokemon={pokemon} />
      <Pagination gotoNextPage={nextPageURL ? gotoNextPage : null} gotoPrevPage={prevPageURL ? gotoPrevPage : null} />
    </>
  );
}

export default App;
