"use client";

import CheckboxField from "./CheckboxField";
import DateField from "./DateField";
import EmailField from "./EmailField";
import MultiSelectField from "./MultiSelectField";
import NumberField from "./NumberField";
import SelectField from "./SelectField";
import TextareaField from "./TextareaField";
import TextField from "./TextField";

interface FieldMapperProps {
  field: any;
  value: any;
  onChange: (value: any) => void;
  error?: string;
}

export default function FieldMapper({
  field,
  value,
  onChange,
  error,
}: FieldMapperProps) {
  const commonProps = {
    name: field.name,
    label: field.label,
    required: field.required,
    placeholder: field.placeholder,
    value: value || "",
    onChange: onChange,
    error: error,
  };

  switch (field.type) {
    case "text":
      return <TextField {...commonProps} />;
    case "email":
      return <EmailField {...commonProps} />;
    case "textarea":
      return <TextareaField {...commonProps} rows={field.rows || 3} />;
    case "select":
      return <SelectField {...commonProps} options={field.options || []} />;
    case "multiselect":
      return (
        <MultiSelectField {...commonProps} options={field.options || []} />
      );
    case "number":
      return <NumberField {...commonProps} min={field.min} max={field.max} />;
    case "date":
      return <DateField {...commonProps} />;
    case "checkbox":
      return <CheckboxField {...commonProps} />;
    default:
      return <TextField {...commonProps} />;
  }
}
