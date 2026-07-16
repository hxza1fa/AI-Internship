"use client";

import TextButton from "@/components/text-button";
import { useState } from "react";

const cut_strings = [
  "Ideal",
  "Premium",
  "Very Good",
  "Good",
  "Fair",
];

const clarity_strings = [
  "I1",
  "SI2",
  "SI1",
  "VS2",
  "VS1",
  "VVS2",
  "VVS1",
  "IF",
];

type TextGridProps = {
  type: "cut" | "clarity";
  value: string;
  onSelect: (value: string) => void;
};

export default function TextGrid({ type }: TextGridProps) {
  const [selectedText, setSelectedText] = useState("");

  const buttons = type === "cut" ? cut_strings : clarity_strings;

  return (
    <div className="flex flex-wrap justify-center gap-3">
      {buttons.map((text) => (
        <TextButton
          key={text}
          text={text}
          selected={selectedText === text}
          onSelect={setSelectedText}
        />
      ))}
    </div>
  );
}