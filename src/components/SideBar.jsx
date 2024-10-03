import React from "react";
import { Link } from "react-router-dom";
function SideBar({ method_list }) {

    return (
        <aside className="w-1/6 h-[93vh] flex flex-col pt-8 p-4 border-r-2 border-dotted border-[#c2c2c2]">
            {
                method_list.map((m) => (
                    <li className="mb-2 hover:text-[#00509d] transition-colors ease-out">
                        <Link to={`/${m[1]}`} className="text-xl w-full h-10">{m[0]}</Link>
                    </li>
                ))
            }
        </aside>
    )
}


export default SideBar;
