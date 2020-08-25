import React from 'react';

export default function PokeList(props) {
    return (
        <div id="PokeList">
            {props.pokemon.map(p => <h4 key={p}>{p}</h4>)}
        </div>
    );
}