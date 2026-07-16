"use client";

import ColorButton from "@/components/color-button";

type ColorGridProps = {
  value: string;
  onSelect: (color: string) => void;
};

const diamondColors = [
  { grade: "D", color: "#ffffff" },
  { grade: "E", color: "#fafafa" },
  { grade: "F", color: "#f8f7f2" },
  { grade: "G", color: "#f5f2e8" },
  { grade: "H", color: "#f1ead7" },
  { grade: "I", color: "#ede2c7" },
  { grade: "J", color: "#f5f0dc" },
];

export default function ColorGrid({
  value,
  onSelect,
}: ColorGridProps) {
  return (
    <div className="flex justify-center gap-4">
      {diamondColors.map(({ grade, color }) => (
        <ColorButton
          key={grade}
          color={color}
          grade={grade}
          selected={value === grade}
          onSelect={onSelect}
        />
      ))}
    </div>
  );
}