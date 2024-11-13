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
        <div className="w-1/6 h-screen flex flex-col p-4 pl-6 border-r-2 border-dotted border-[#c2c2c2]">
            <div className="w-full h-fit flex items-center">
                <Link to="/" className="text-3xl w-fit h-fit flex items-center pb-1 mt-4 mb-3 mr-2 text-[#00509d]">Crystal</Link>
                <svg className="w-8 h-8 flex items-center pt-1.5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#00509d" d="M116.7 33.8c4.5-6.1 11.7-9.8 19.3-9.8l240 0c7.6 0 14.8 3.6 19.3 9.8l112 152c6.8 9.2 6.1 21.9-1.5 30.4l-232 256c-4.5 5-11 7.9-17.8 7.9s-13.2-2.9-17.8-7.9l-232-256c-7.7-8.5-8.3-21.2-1.5-30.4l112-152zm38.5 39.8c-3.3 2.5-4.2 7-2.1 10.5l57.4 95.6L63.3 192c-4.1 .3-7.3 3.8-7.3 8s3.2 7.6 7.3 8l192 16c.4 0 .9 0 1.3 0l192-16c4.1-.3 7.3-3.8 7.3-8s-3.2-7.6-7.3-8L301.5 179.8l57.4-95.6c2.1-3.5 1.2-8.1-2.1-10.5s-7.9-2-10.7 1L256 172.2 165.9 74.6c-2.8-3-7.4-3.4-10.7-1z" /></svg>
            </div>
            <nav className="mt-6">
                {Object.entries(chapters).map(([chapter, functions]) => (
                    <div key={chapter} className="mb-4">
                        <h3
                            className="hover:text-[#00509d] hover:translate-x-3"
                            onClick={() => handleChapterClick(chapter)}
                        >
                            {chapter}
                        </h3>
                        {expandedChapter === chapter && (
                            <ul>
                                {functions.map(([label, path, type]) => (
                                    <li key={path} className="hover:text-[#00509d] hover:translate-x-3">
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