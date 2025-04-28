import React, { useState } from 'react';
import NoteCard from './components/NoteCard';
import './styles/App.css';

const App = () => {
    const [notes, setNotes] = useState([
        { id: 1, content: 'First note' },
        { id: 2, content: 'Second note' },
        { id: 3, content: 'Third note' },
    ]);

    return (
        <div className="app">
            <h1>Notes</h1>
            <div className="notes-container">
                {notes.map(note => (
                    <NoteCard key={note.id} content={note.content} />
                ))}
            </div>
        </div>
    );
};

export default App;