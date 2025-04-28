import React from 'react';
import './NoteCard.css';

const NoteCard = ({ title, content }) => {
    return (
        <div className="note-card">
            <h2 className="note-title">{title}</h2>
            <p className="note-content">{content}</p>
        </div>
    );
};

export default NoteCard;