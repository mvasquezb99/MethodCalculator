import React, { useEffect, useState } from "react";
import axios from "axios";
import MethodForm from "./MethodForm";
import Table from "./Table";

function Method({ method_route, method_name }) {
    const [method_data, setMethod_data] = useState({});
    const [method_answer, setMethod_answer] = useState(undefined);
    const [calculator, set_calculator] = useState(undefined);
    const [imageSrc, setImageSrc] = useState(""); 

    const get_method = async () => {
        const res = await axios.get(`http://localhost:5000/${method_route}`);
        setMethod_data(res.data);
        console.log(res.data);
    };

    const put_method = async (input) => {
        try {
            const ans = await axios.post(`http://localhost:5000/${method_route}`, { input });
            console.log("Respuesta del servidor:", ans.data);
            setMethod_answer(ans.data);
            calculator.setExpression({ id: 'AnswGraph', latex: `f(x) = ${input.fx}` });
            calculator.setExpression({ id: 'AnswPoint', latex: `x = ${ans.data.Xm[ans.data.Xm.length - 1]}`, lineStyle: Desmos.Styles.DASHED });
            calculator.asyncScreenshot(
                {
                    mode: 'preserveX',
                    width: 500,
                    height: 300,
                    mathBounds: { left: -5, right: 5 } 
                },
                (data) => setImageSrc(data) 
            );
        } catch (error) {
            console.error("Error en la solicitud POST:", error);
        }
    };

    const create_desmos = () => {
        let container = document.getElementById("calculatorWrapper");
        let calcContainer = document.createElement("div");

        calcContainer.id = 'calculator';
        calcContainer.classList.add("w-full", "h-96", "pt-4");
        container.appendChild(calcContainer);

        let elt = document.getElementById("calculator");
        set_calculator(Desmos.GraphingCalculator(elt));
    };

    const destroy_desmos = () => {
        let elt = document.getElementById("calculator");
        elt.remove();
    };

    useEffect(() => {
        get_method();
        if (document.getElementById("calculator") !== null) {
            destroy_desmos();
        }
        create_desmos();
        setMethod_answer(undefined);
        setMethod_data({});
    }, [method_route]);

    return (
        <main className="w-full h-[93vh] p-6 overflow-y-scroll">
            <h1 className="w-fit text-start text-5xl mb-3 text-[#00509d]">
                {method_name}
            </h1>
            <h2 className="text-2xl text-gray-500 text-opacity-100">Explicación</h2>
            <p className="mt-3 border-b-2 border-dotted pb-6 w-fit text-justify">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aspernatur suscipit corporis, fugit ad nulla reiciendis quaerat expedita similique culpa necessitatibus, inventore doloremque labore illum, commodi incidunt qui excepturi iure exercitationem!
                Voluptates aliquid nemo temporibus! Quam, amet aliquid. Tenetur harum consequuntur nostrum vitae omnis excepturi animi magnam facere, eum maxime nihil culpa, reprehenderit illum! Necessitatibus incidunt eum, maxime laboriosam sed cumque?
            </p>
            <h2 className="text-2xl text-gray-500 text-opacity-100 mt-3">Calculadora</h2>
            <section className="w-full h-[51vh] flex mt-4 pb-4 justify-evenly border-b-2 border-dotted">
                <MethodForm method_obj={method_data} put_method={put_method} />
                <Table data={method_answer} method_name={method_name} />
            </section>
            <section className="w-full h-[93vh] flex mt-3 justify-evenly ">
                <div id='calculatorWrapper' className="h-full w-full flex flex-col items-start justify-start">
                    <h2 className="text-2xl text-gray-500 text-opacity-100">Grafica</h2>
                    {imageSrc && (
                        <a
                            href={imageSrc}
                            download="graph-screenshot.png"
                            className="mt-4 p-2 bg-green-500 text-white rounded"
                        >
                            Descargar Imagen
                        </a>
                    )} 
                </div>
            </section>
        </main>
    );
}

export default Method;
