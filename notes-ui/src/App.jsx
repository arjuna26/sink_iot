import React, { useEffect, useState } from 'react';
import NoteCard from './NoteCard.jsx';
import './App.css';

const BUCKET = 'cpsc341-text';

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    fetch('http://10.0.0.38:5000/api/notes')
      .then(res => res.json())
      .then(files => Promise.all(
        files.map(filename =>
          fetch(`https://storage.googleapis.com/${BUCKET}/${filename}`)
            .then(res => res.text())
            .then(content => ({
              id: filename,
              title: filename,
              content,
            }))
        )
      ))
      .then(setNotes)
      .catch(err => {
        console.error("Failed to fetch notes:", err);
      });
  }, []);

  return (
    <div className="app">
      <h1>Notes</h1>
      <div className="notes-container">
        {notes.map(note => (
          <NoteCard key={note.id} title={note.title} content={note.content} />
        ))}
      </div>
    </div>
  );
}

export default App;