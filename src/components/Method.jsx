import React, { useEffect, useState } from "react";
import axios from "axios";
import MethodForm from "./MethodForm";
import Table from "./Table";
import { parse, all, create, log } from 'mathjs';

function Method({ method_route, method_name, get_active_method, type }) {
    const [method_data, setMethod_data] = useState({});
    const [method_answer, setMethod_answer] = useState(undefined);
    const [calculator, set_calculator] = useState(undefined);

    const get_method = async () => {
        const res = await axios.get(`http://localhost:5000/${method_route}`);
        setMethod_data(res.data);
    }

    const put_method = async (input) => {
        input["use_cs"] = "on" ? "1" : "0";

        const ans = await axios.post(`http://localhost:5000/${method_route}`, { input })
        setMethod_answer(ans.data);

        const math = create(all);
        if(type === "regular"){
            let func = input.fx;
            func = func.replace(/\*\*/g, '^');
            const node = math.parse(func);
            const latex = node.toTex();
            calculator.setExpression({ id: 'AnswGraph', latex: `f(x) = ${latex}` });
            calculator.setExpression({ id: 'AnswPoint', latex: `x = ${ans.data.Xm[ans.data.Xm.length - 1]}`, lineStyle: Desmos.Styles.DASHED });
        } else if(type === "matrix"){
            let matrix = input["A"].split(";");
            if(matrix.length === 2){
                let matrix_cpy = matrix;
                let b = input["b"].split(";");
                console.log(matrix);
                
                for(let i = 0; i < matrix.length ; i++){
                    matrix_cpy = matrix[i].split(" ");
                    calculator.setExpression({ id: `AnswGraph_${i}`, latex: `${matrix_cpy[0]}x + ${matrix_cpy[1]}y = ${b[i]}` });
                }
            }
        }

    }

    const create_desmos = () => {
        let container = document.getElementById("calculatorWrapper")
        let calcContainer = document.createElement("div")

        calcContainer.id = 'calculator'
        calcContainer.classList.add("w-full", "h-[500px]", "pt-4")
        container.appendChild(calcContainer);

        let elt = document.getElementById("calculator");
        set_calculator(Desmos.GraphingCalculator(elt));
    }

    const destroy_desmos = () => {
        let elt = document.getElementById("calculator")
        elt.remove()
    }

    function svg_cb(data) {
        const blob = new Blob([data], { type: 'image/svg+xml' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');

        link.href = url;
        link.download = 'image.svg';

        document.body.appendChild(link);
        link.click();

        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }

    const get_svg_graph = () => {
        calculator.asyncScreenshot({
            format: 'svg',
        }, svg_cb);
    }

    const handle_active_method = () => {
        get_active_method(method_name);
    }

    useEffect(() => {
        handle_active_method();
        get_method();
        if (document.getElementById("calculator") !== null) {
            destroy_desmos()
        }
        create_desmos()
        setMethod_answer(undefined);
        setMethod_data({});
    }, [method_route])


    return (
        <main className="w-full h-screen p-6 overflow-y-scroll">
            <h1 className="w-fit text-start text-5xl mb-3 text-[#00509d]">
                {method_name}
            </h1>
            <h2 className="text-2xl text-gray-500 text-opacity-100">Explicación</h2>
            <p className="mt-3 border-b-2 border-dotted pb-6 w-fit text-justify">
                {method_data["explicacion"]}
            </p>
            <h2 className="text-2xl text-gray-500 text-opacity-100 mt-3">Calculadora</h2>
            <section className="w-full h-[51vh] flex mt-4 pb-4 justify-evenly border-b-2 border-dotted">
                <MethodForm method_obj={method_data} put_method={put_method} method_type={type}/>
                <Table data={method_answer} type={type} />
            </section>
            <section className="w-full h-[93vh] flex flex-col mt-3 justify-start items-start ">
                <div id='calculatorWrapper' className="h-fit w-full flex flex-col items-start justify-start">
                    <h2 className="text-2xl text-gray-500 text-opacity-100">Grafica</h2>
                </div>
                <button onClick={get_svg_graph} download="graph-screenshot.svg" className="bg-[#00509d] p-1.5 rounded-lg w-fit mt-2 text-white">Descarga el SVG</button>
            </section>
        </main>
    );
}


export default Method;