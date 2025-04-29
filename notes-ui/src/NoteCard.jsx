import React from 'react';

function formatTitle(filename) {
  const base = filename.replace('.txt', '');
  const match = base.match(/^photo_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})$/);
  if (match) {
    const [, year, month, day, hour, min, sec] = match;
    return `${year}-${month}-${day} ${hour}:${min}:${sec}`;
  }
  return base;
}

export default function NoteCard({ title, content }) {
  return (
    <div className="note-card">
      <div className="note-header">
        <h2>{formatTitle(title)}</h2>
      </div>
      <div className="note-content">
        <pre>{content}</pre>
      </div>
    </div>
  );
}