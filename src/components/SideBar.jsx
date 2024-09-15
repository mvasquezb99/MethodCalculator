import React from "react";
import { Link } from "react-router-dom";
function SideBar({ method_list }) {
    return (
        <aside className="w-1/6 h-screen flex flex-col pt-8 p-4 border-r-2 border-dotted border-[#c2c2c2]">
            {
                method_list.map(m => (
                    <Link to={`/${m}`} className="text-xl w-full h-10 mb-1 hover:text-[#c2c2c2] transition-colors ease-out"> - {m}</Link>
                ))
            }
        </aside>
    )
}


export default SideBar;
