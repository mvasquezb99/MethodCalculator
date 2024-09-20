import React, { useEffect } from "react";


function Table({ data, method_name }) {

    return (
        <div className="w-1/2 h-96 border border-[#c2c2c2] rounded-md p-2 overflow-y-scroll">
            {
                data !== undefined ?
                    <table className="table-fixed w-full h-full">
                        <thead className="border-b border-dotted border-[#c2c2c2]">
                            <tr>
                                <th className="text-start">Evaluaciones f(x)</th>
                                <th className="text-start ">Valores de Xn</th>
                                <th className="text-start ">Error absoluto</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                data.fxm.map((fx, i) => (
                                    <tr className="border-b border-dotted border-[#c2c2c2] pb-1 last:text-[#00509d] last:border-none">
                                        <td className="text-start">{fx}</td>
                                        <td className="text-start">{data.Xm[i]}</td>
                                        <td className="text-start">{data.E[i]}</td>
                                    </tr>
                                ))
                            }
                        </tbody>
                    </table> :
                    <>
                        <div className="w-full h-full flex justify-center items-center">
                            <h1 className="text-3xl">Esperando por tus entradas!</h1>
                        </div>
                    </>
            }
        </div>
    )
}

export default Table;