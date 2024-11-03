import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Sidebar = ({ chapters }) => {
    const [expandedChapter, setExpandedChapter] = useState(null);
    const handleChapterClick = (chapter) => {
        setExpandedChapter(expandedChapter === chapter ? null : chapter);
    };

    if (!chapters) {
        return <div>No hay capítulos disponibles.</div>;
    }

    return (
        <div className="w-64 h-full bg-gray-800 text-white">
            <Link to="/" className="block p-4 text-2xl font-bold hover:bg-gray-700">
                Análisis Numérico
            </Link>
            <nav className="mt-6">
                {Object.entries(chapters).map(([chapter, functions]) => (
                    <div key={chapter} className="mb-4">
                        <h3
                            className="text-lg font-semibold cursor-pointer hover:bg-gray-700 p-2"
                            onClick={() => handleChapterClick(chapter)}
                        >
                            {chapter}
                        </h3>
                        {expandedChapter === chapter && (
                            <ul>
                                {functions.map(([label, path, type]) => (
                                    <li key={path} className="hover:bg-gray-700">
                                        <Link to={`/${path}`} className="block py-2 px-4">
                                            {label}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        )}
                    </div>
                ))}
            </nav>
        </div>
    );
};

export default Sidebar;
