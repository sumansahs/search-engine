import React from 'react';

function ResultsList({ results }) {
  return (
    <ul>
      {results.map((result, index) => (
        <li key={index}>
          <a href={result.link}>{result.title}</a>
          <p>{result.snippet}</p>
        </li>
      ))}
    </ul>
  );
}

export default ResultsList;
