"use client";

import { useState } from "react";

interface SelectOption {
  value: string;
  label: string;
}

interface MultiSelectFieldProps {
  name: string;
  label: string;
  required?: boolean;
  placeholder?: string;
  value: string[];
  onChange: (value: string[]) => void;
  error?: string;
  options: SelectOption[];
}

export default function MultiSelectField({
  name,
  label,
  required = false,
  placeholder,
  value = [],
  onChange,
  error,
  options,
}: MultiSelectFieldProps) {
  const [isFocused, setIsFocused] = useState(false);

  const handleOptionToggle = (optionValue: string) => {
    const newValue = value.includes(optionValue)
      ? value.filter((v) => v !== optionValue)
      : [...value, optionValue];
    onChange(newValue);
  };

  return (
    <div className="mb-4">
      <label className="block text-sm font-medium text-gray-700 mb-1">
        {label}
        {required && <span className="text-red-500 ml-1">*</span>}
      </label>
      <div
        className={`w-full px-3 py-2 border rounded-md focus-within:outline-none focus-within:ring-2 focus-within:ring-blue-500 focus-within:border-transparent text-sm transition-colors ${
          error
            ? "border-red-500 focus-within:ring-red-500"
            : isFocused
            ? "border-blue-500"
            : "border-gray-300"
        }`}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
      >
        {value.length === 0 && (
          <span className="text-gray-500">
            {placeholder || "Select options"}
          </span>
        )}
        <div className="flex flex-wrap gap-1 mt-1">
          {value.map((selectedValue) => {
            const option = options.find((opt) => opt.value === selectedValue);
            return (
              <span
                key={selectedValue}
                className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
              >
                {option?.label || selectedValue}
                <button
                  type="button"
                  onClick={() => handleOptionToggle(selectedValue)}
                  className="ml-1 inline-flex items-center justify-center w-4 h-4 rounded-full text-blue-400 hover:bg-blue-200 hover:text-blue-500 focus:outline-none"
                >
                  ×
                </button>
              </span>
            );
          })}
        </div>
        <div className="mt-2 space-y-1">
          {options.map((option) => (
            <label
              key={option.value}
              className="flex items-center space-x-2 cursor-pointer hover:bg-gray-50 p-1 rounded"
            >
              <input
                type="checkbox"
                checked={value.includes(option.value)}
                onChange={() => handleOptionToggle(option.value)}
                className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
              />
              <span className="text-sm">{option.label}</span>
            </label>
          ))}
        </div>
      </div>
      {error && <p className="mt-1 text-sm text-red-600">{error}</p>}
    </div>
  );
}
