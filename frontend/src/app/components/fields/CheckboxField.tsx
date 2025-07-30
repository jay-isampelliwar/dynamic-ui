"use client";

interface CheckboxFieldProps {
  name: string;
  label: string;
  required?: boolean;
  value: boolean;
  onChange: (value: boolean) => void;
  error?: string;
}

export default function CheckboxField({
  name,
  label,
  required = false,
  value,
  onChange,
  error,
}: CheckboxFieldProps) {
  return (
    <div className="mb-4">
      <label className="flex items-center space-x-2 cursor-pointer">
        <input
          type="checkbox"
          id={name}
          name={name}
          checked={value}
          onChange={(e) => onChange(e.target.checked)}
          required={required}
          className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
        />
        <span className="text-sm font-medium text-gray-700">
          {label}
          {required && <span className="text-red-500 ml-1">*</span>}
        </span>
      </label>
      {error && <p className="mt-1 text-sm text-red-600">{error}</p>}
    </div>
  );
}
