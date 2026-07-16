"use client";

import { useState, type CSSProperties } from "react";
import localFont from "next/font/local";
import ColorGrid from "@/components/color-grid";
import TextGrid from "@/components/text-grid";
import PredictButton from "@/components/predict-button";

export async function postDiamond(data: any) {
  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  console.log("Status:", response.status);

  const text = await response.text();
  console.log("Raw response:", text);

  return JSON.parse(text);
}

const dmSansBold = localFont({
  src: "../../fonts/dm-sans/DMSans_36pt-Bold.ttf",
  display: "swap",
});

const dmSansRegular = localFont({
  src: "../../fonts/dm-sans/DMSans_18pt-Regular.ttf",
  display: "swap",
});

const dimensionFields = [
  {
    label: "Carat",
    name: "carat" as const,
    hint: "e.g. 0.75",
    min: 0.2,
    max: 5,
    step: 0.01,
    defaultValue: 0.75,
  },
  {
    label: "X",
    name: "x" as const,
    hint: "e.g. 5.85 mm",
    min: 0,
    max: 10,
    step: 0.01,
    defaultValue: 5.85,
  },
  {
    label: "Y",
    name: "y" as const,
    hint: "e.g. 5.87 mm",
    min: 0,
    max: 10,
    step: 0.01,
    defaultValue: 5.87,
  },
  {
    label: "Z",
    name: "z" as const,
    hint: "e.g. 3.63 mm",
    min: 0,
    max: 10,
    step: 0.01,
    defaultValue: 3.63,
  },
];

const proportionFields = [
  {
    label: "Depth",
    name: "depth" as const,
    hint: "e.g. 61.5%",
    min: 40,
    max: 80,
    step: 0.1,
    defaultValue: 61.5,
  },
  {
    label: "Table",
    name: "table" as const,
    hint: "e.g. 57%",
    min: 40,
    max: 90,
    step: 0.1,
    defaultValue: 57,
  },
];

type DimensionName = (typeof dimensionFields)[number]["name"];

export default function PredictPage() {
  const [values, setValues] = useState<Record<DimensionName, number>>({
    carat: 0.75,
    x: 5.85,
    y: 5.87,
    z: 3.63,
  });

  const [diamondColor, setDiamondColor] = useState("D");
  const [cut, setCut] = useState("Fair");
  const [clarity, setClarity] = useState("I1");
  const [predictedPrice, setPredictedPrice] = useState<number | null>(null);

  const [proportions, setProportions] = useState({
    depth: 61.5,
    table: 57,
  });

  const handlePredict = async () => {
    const diamond = {
      carat: values.carat,
      cut: cut,
      color: diamondColor,
      clarity: clarity,
      depth: proportions.depth,
      table: proportions.table,
      x: values.x,
      y: values.y,
      z: values.z
    }

    console.log(diamond);
    const response = await postDiamond(diamond);

    setPredictedPrice(response.price)
  };

  const updateValue = (name: DimensionName, next: number) => {
    if (Number.isNaN(next)) return;
    setValues((prev) => ({ ...prev, [name]: next }));
  };

  const updateProportion = (
    name: "depth" | "table",
    next: number
  ) => {
    if (Number.isNaN(next)) return;

    setProportions((prev) => ({
      ...prev,
      [name]: next,
    }));
  };

  return (
    <section className="p-8">
      <div className="mb-8 pt-8 text-center">
        <h1
          className={`${dmSansBold.className} text-[#f5f5f5] text-[36px] tracking-tight`}
        >
          Build Your Diamond
        </h1>
      </div>
      <div className="mx-auto h-[75vh] w-[85%] overflow-y-auto rounded-lg bg-white p-8 shadow-lg">
        <div className="flex flex-col">
          <h2
            className={`${dmSansBold.className} text-left text-[28px] text-[#1e3a8a] tracking-tight`}
          >
            Diamond Dimensions
          </h2>
          <div className="mt-6 flex gap-4">
            {dimensionFields.map(({ label, name, hint, min, max, step }) => (
              <div
                key={name}
                className="flex min-h-28 flex-1 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm"
              >
                <label
                  htmlFor={name}
                  className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
                >
                  {label}
                </label>
                <input
                  id={name}
                  name={name}
                  type="number"
                  step={step}
                  min={min}
                  max={max}
                  value={values[name]}
                  placeholder={hint}
                  onChange={(e) => updateValue(name, Number(e.target.value))}
                  className={`${dmSansRegular.className} w-full rounded-md border border-[#e5e7eb] bg-white px-3 py-2 text-[14px] text-[#111827] placeholder:text-[#9ca3af] outline-none focus:border-[#1e3a8a]`}
                />
                <input
                  type="range"
                  min={min}
                  max={max}
                  step={step}
                  value={values[name]}
                  onChange={(e) => updateValue(name, Number(e.target.value))}
                  aria-label={`${label} slider`}
                  className="diamond-slider w-full"
                  style={
                    {
                      "--slider-progress": `${((values[name] - min) / (max - min)) * 100}%`,
                    } as CSSProperties
                  }
                />
              </div>
            ))}
          </div>
        </div>

        <div className="mt-10 flex flex-col">
          <h2
            className={`${dmSansBold.className} text-left text-[28px] text-[#1e3a8a] tracking-tight`}
          >
            Diamond Quality
          </h2>

          <div className="mt-6 items-center flex gap-4">
            <div className="flex min-h-32 flex-1 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm">
              <span
                className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
              >
                Cut
              </span>
              <TextGrid
                type="cut"
                value={cut}
                onSelect={setCut} />
            </div>

            <div className="flex min-h-32 flex-1 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm">
              <span
                className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
              >
                Color
              </span>
              <ColorGrid
                value={diamondColor}
                onSelect={setDiamondColor} />
            </div>

            <div className="flex min-h-32 flex-1 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm">
              <span
                className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
              >
                Clarity
              </span>
              <TextGrid
                type="clarity"
                value={clarity}
                onSelect={setClarity} />
            </div>
          </div>
        </div>

        <div className="mt-10 flex flex-col">
          <h2
            className={`${dmSansBold.className} text-left text-[28px] text-[#1e3a8a] tracking-tight`}
          >
            Diamond Proportions
          </h2>
          <div className="mt-6 max-w-186 grid grid-cols-2 gap-4">
            {proportionFields.map(({ label, name, hint, min, max, step }) => (
              <div
                key={name}
                className="flex min-h-28 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm"
              >
                <label
                  htmlFor={name}
                  className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
                >
                  {label}
                </label>

                <input
                  id={name}
                  name={name}
                  type="number"
                  step={step}
                  min={min}
                  max={max}
                  value={proportions[name]}
                  placeholder={hint}
                  onChange={(e) =>
                    updateProportion(name, Number(e.target.value))
                  }
                  className={`${dmSansRegular.className} w-full rounded-md border border-[#e5e7eb] bg-white px-3 py-2 text-[14px] text-[#111827] placeholder:text-[#9ca3af] outline-none focus:border-[#1e3a8a]`}
                />

                <input
                  type="range"
                  min={min}
                  max={max}
                  step={step}
                  value={proportions[name]}
                  onChange={(e) =>
                    updateProportion(name, Number(e.target.value))
                  }
                  aria-label={`${label} slider`}
                  className="diamond-slider w-full"
                  style={
                    {
                      "--slider-progress": `${((proportions[name] - min) / (max - min)) * 100}%`,
                    } as CSSProperties
                  }
                />
              </div>
            ))}
          </div>
        </div>
        <PredictButton onClick={handlePredict} />

        <div className="flex justify-center items-center pt-8">
          {predictedPrice !== null && (
            <h2 className={`${dmSansBold.className} text-3xl text-green-600`}>
              Predicted Price: ${predictedPrice}
            </h2>
          )}
        </div>
      </div>
    </section>
  );
}
