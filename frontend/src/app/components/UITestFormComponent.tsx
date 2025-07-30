"use client";

import { useState } from "react";
import { FormComponent } from "../lib";
import FieldMapper from "./fields/FieldMapper";

interface UITestFormComponentProps {
  component: FormComponent;
}

export default function UITestFormComponent({
  component,
}: UITestFormComponentProps) {
  const [formData, setFormData] = useState<Record<string, any>>({});
  const [errors, setErrors] = useState<Record<string, string>>({});

  // Validate component structure
  if (!component || !component.fields || !Array.isArray(component.fields)) {
    console.error("Invalid component structure:", component);
    return (
      <div className="bg-red-50 border border-red-200 rounded-lg p-4">
        <p className="text-red-600">Error: Invalid form component structure</p>
      </div>
    );
  }

  const handleInputChange = (fieldName: string, value: any) => {
    setFormData((prev) => ({
      ...prev,
      [fieldName]: value,
    }));
  };

  const validate = () => {
    const newErrors: Record<string, string> = {};
    component.fields.forEach((field) => {
      const value = formData[field.name];
      if (field.required) {
        if (field.type === "multiselect") {
          if (!Array.isArray(value) || value.length === 0) {
            newErrors[field.name] = `${field.label} is required.`;
          }
        } else if (!value || value === "") {
          newErrors[field.name] = `${field.label} is required.`;
        }
      }
      if (field.type === "email" && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
          newErrors[field.name] = "Invalid email address.";
        }
      }
      if (field.type === "number" && value !== undefined && value !== "") {
        if (isNaN(Number(value))) {
          newErrors[field.name] = `${field.label} must be a valid number.`;
        }
      }
    });
    return newErrors;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const validationErrors = validate();
    setErrors(validationErrors);
    if (Object.keys(validationErrors).length > 0) {
      return;
    }
    console.log("Form submitted with data:", formData);
    alert("Form submitted!\n" + JSON.stringify(formData, null, 2));
  };

  const renderField = (field: any) => {
    // Validate field structure
    if (!field || !field.name || !field.type) {
      console.error("Invalid field structure:", field);
      return (
        <div className="text-red-600 text-sm">
          Error: Invalid field structure
        </div>
      );
    }

    return (
      <FieldMapper
        field={field}
        value={formData[field.name]}
        onChange={(value) => handleInputChange(field.name, value)}
        error={errors[field.name]}
      />
    );
  };

  return (
    <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
      <form onSubmit={handleSubmit} className="space-y-4">
        {component.fields.map((field, index) => (
          <div key={index}>
            <label
              htmlFor={field.name}
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              {field.label}
              {field.required && <span className="text-red-500 ml-1">*</span>}
            </label>
            {renderField(field)}
          </div>
        ))}
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
        >
          {component.submitText || "Submit"}
        </button>
      </form>
    </div>
  );
}
