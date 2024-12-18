import React, { useEffect } from "react";


function Table({ data, type }) {

    return (
        <div className="w-1/2 h-[425px] border border-[#c2c2c2] rounded-md p-2 overflow-y-scroll">
            {
                data !== undefined && data.status === 200 ?
                    <table className="table-fixed w-full h-full">
                        <thead className="border-b border-dotted border-[#c2c2c2]">
                            <tr>
                                {
                                    type === "regular" ? <>
                                        <th className="text-start">Evaluaciones f(x)</th>
                                        <th className="text-start">Valores de Xn</th>
                                        <th className="text-start">Error absoluto</th>
                                    </> : type === "matrix" ? <>
                                        <th className="text-start">Evaluaciones f(x)</th>
                                        <th className="text-start">Error</th>
                                        <th className="text-start">Radio espectral</th>
                                    </> : <></>
                                }
                            </tr>
                        </thead>
                        {
                            type === "regular" && data !== undefined ? <>
                                <tbody>
                                    {
                                        data.fxm.map((fx, i) => (
                                            <tr className="border-b border-dotted border-[#c2c2c2] pb-1 last:text-[#00509d] last:border-none last:font-semibold">
                                                <td className="text-start overflow-hidden">{fx}</td>
                                                <td className="text-start overflow-hidden">{data.Xm[i]}</td>
                                                <td className="text-start overflow-hidden">{data.E[i]}</td>
                                            </tr>
                                        ))
                                    }
                                </tbody>
                            </> : type === "matrix" && data.S !== undefined ? <>
                                {
                                    data.S.map((S, i) => (
                                        <tr className="border-b border-dotted border-[#c2c2c2] pb-1 last:text-[#00509d] last:border-none last:font-semibold">
                                            <td className="text-start overflow-hidden">
                                                {S.map((e) => (
                                                    e + ""
                                                ))}
                                            </td>
                                            <td className="text-start overflow-hidden">{data.E[i]}</td>
                                            {i === data.S.length-1 ? <td className="text-start font-bold overflow-hidden text-[#00509d]">{data["RE"]}</td>: "" }
                                        </tr>
                                    ))
                                }
                            </> : type === "polinomial" ? <>
                                <div className="w-full h-full flex justify-center items-center">
                                    <h1 className="text-3xl">No tenemos tabla para esto...</h1>
                                </div>
                            </> : <></>
                        }
                    </table> :
                    data === undefined ?
                        <div className="w-full h-full flex justify-center items-center">
                            <h1 className="text-3xl">Esperando por tus entradas!</h1>
                        </div> :
                        data.status === 400 ?
                            <div className="w-full h-full flex flex-col justify-center items-center">
                                <h1 className="text-3xl text-red-700">Oops nos encotramos con un error!</h1>
                                <small className="text-red-700">{data.message}</small>
                            </div> : 
                            <div className="w-full h-full flex flex-col justify-center items-center">
                                <h1 className="text-3xl text-red-700">Oops nos encotramos con un error!</h1>
                            </div>
            } : 
        </div>
    )
}

export default Table;
