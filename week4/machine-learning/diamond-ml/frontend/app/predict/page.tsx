"use client";

import { useState, type CSSProperties } from "react";
import localFont from "next/font/local";

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

type DimensionName = (typeof dimensionFields)[number]["name"];

export default function PredictPage() {
  const [values, setValues] = useState<Record<DimensionName, number>>({
    carat: 0.75,
    x: 5.85,
    y: 5.87,
    z: 3.63,
  });

  const updateValue = (name: DimensionName, next: number) => {
    if (Number.isNaN(next)) return;
    setValues((prev) => ({ ...prev, [name]: next }));
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
                  className="w-full"
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
          <div className="mt-6 flex gap-4">
            {["Cut", "Color", "Clarity"].map((label) => (
              <div
                key={label}
                className="flex min-h-28 flex-1 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm"
              >
                <span
                  className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
                >
                  {label}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="mt-10 flex flex-col">
          <h2
            className={`${dmSansBold.className} text-left text-[28px] text-[#1e3a8a] tracking-tight`}
          >
            Diamond Proportions
          </h2>
          <div className="mt-6 grid grid-cols-4 gap-4">
            {["Depth", "Table"].map((label) => (
              <div
                key={label}
                className="flex min-h-28 flex-col gap-3 rounded-lg border border-[#e5e7eb] bg-[#f5f5f5] p-4 shadow-sm"
              >
                <span
                  className={`${dmSansRegular.className} text-[16px] text-[#111827]`}
                >
                  {label}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
