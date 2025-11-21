import React from 'react';
import { ArrowRight, ArrowLeft, ArrowDown, ArrowUp } from 'lucide-react';

const ClinicEnterpriseDiagram = () => {
  return (
    <div className="w-full max-w-7xl mx-auto p-6 bg-gray-50">
      <h1 className="text-3xl font-bold text-center mb-2 text-red-800">
        Family-Care Medical Clinic
      </h1>
      <h2 className="text-xl text-center mb-6 text-gray-700">
        Enterprise System Diagram
      </h2>

      <div className="relative bg-white p-8 rounded-lg shadow-lg">

        {/* Environment Bar */}
        <div className="absolute top-0 left-0 right-0 bg-purple-200 p-4 rounded-t-lg border-2 border-purple-400">
          <h3 className="text-center font-bold text-lg">ENVIRONMENT</h3>
          <p className="text-center text-sm">Healthcare regulations, insurance policies, community health needs</p>
        </div>

        <div className="mt-20 grid grid-cols-12 gap-4">

          {/* INPUTS Column */}
          <div className="col-span-3 space-y-4">
            <div className="bg-blue-200 p-4 rounded-lg border-2 border-blue-400">
              <h3 className="font-bold text-center mb-4 text-lg">INPUTS</h3>

              <div className="space-y-3">
                <div className="bg-blue-100 p-3 rounded border border-blue-300">
                  <p className="font-semibold">Healthcare Professionals Market</p>
                  <p className="text-sm text-blue-700">→ doctors, nurses, staff</p>
                </div>

                <div className="bg-blue-100 p-3 rounded border border-blue-300">
                  <p className="font-semibold">Medical Suppliers</p>
                  <p className="text-sm text-blue-700">→ equipment, medicines, supplies</p>
                </div>

                <div className="bg-blue-100 p-3 rounded border border-blue-300">
                  <p className="font-semibold">Insurance Companies</p>
                  <p className="text-sm text-blue-700">→ payment agreements</p>
                </div>

                <div className="bg-blue-100 p-3 rounded border border-blue-300">
                  <p className="font-semibold">Technology Vendors</p>
                  <p className="text-sm text-blue-700">→ EMR systems, diagnostic tools</p>
                </div>

                <div className="bg-blue-100 p-3 rounded border border-blue-300">
                  <p className="font-semibold">Capital/Banks</p>
                  <p className="text-sm text-blue-700">→ financing, loans</p>
                </div>
              </div>
            </div>
          </div>

          {/* INTERNAL SYSTEM Column */}
          <div className="col-span-6">
            <div className="bg-red-100 p-4 rounded-lg border-4 border-red-500 min-h-full">
              <h3 className="font-bold text-center mb-4 text-lg">CLINIC INTERNAL SYSTEM</h3>

              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="bg-red-200 p-3 rounded-lg border-2 border-red-400">
                  <p className="font-bold text-center">Human Resources</p>
                  <p className="text-xs text-center mt-1">Hiring, training, scheduling</p>
                </div>

                <div className="bg-red-200 p-3 rounded-lg border-2 border-red-400">
                  <p className="font-bold text-center">Patient Registration</p>
                  <p className="text-xs text-center mt-1">Check-in, records, insurance verification</p>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="bg-pink-200 p-4 rounded-lg border-2 border-pink-400">
                  <p className="font-bold text-center mb-2">Clinical Operations</p>
                  <div className="space-y-1 text-sm">
                    <p>• Examination</p>
                    <p>• Diagnosis</p>
                    <p>• Treatment</p>
                    <p>• Lab work</p>
                  </div>
                </div>

                <div className="bg-red-200 p-3 rounded-lg border-2 border-red-400">
                  <p className="font-bold text-center">Pharmacy Services</p>
                  <p className="text-xs text-center mt-1">Prescriptions, dispensing</p>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4 mb-4">
                <div className="bg-red-200 p-3 rounded-lg border-2 border-red-400">
                  <p className="font-bold text-center">Finance & Billing</p>
                  <p className="text-xs text-center mt-1">Insurance claims, payments, accounts</p>
                </div>

                <div className="bg-red-200 p-3 rounded-lg border-2 border-red-400">
                  <p className="font-bold text-center">Medical Records</p>
                  <p className="text-xs text-center mt-1">EMR, data management</p>
                </div>
              </div>

              <div className="bg-red-200 p-3 rounded-lg border-2 border-red-400">
                <p className="font-bold text-center">Facility Management</p>
                <p className="text-xs text-center mt-1">Maintenance, supplies, equipment</p>
              </div>

              {/* Internal Flows */}
              <div className="mt-4 text-xs text-gray-700 space-y-1">
                <p>↔ patient records flow</p>
                <p>↔ billing information</p>
                <p>↔ staff schedules</p>
                <p>↔ resource allocation</p>
              </div>
            </div>
          </div>

          {/* OUTPUTS Column */}
          <div className="col-span-3 space-y-4">
            <div className="bg-green-200 p-4 rounded-lg border-2 border-green-400">
              <h3 className="font-bold text-center mb-4 text-lg">OUTPUTS</h3>

              <div className="space-y-3">
                <div className="bg-green-100 p-3 rounded border border-green-400">
                  <p className="font-semibold">Patients/Families</p>
                  <p className="text-sm text-green-700">← healthcare services</p>
                  <p className="text-sm text-green-700">← prescriptions</p>
                  <p className="text-sm text-green-700">← health records</p>
                  <p className="text-xs text-green-600 mt-1">→ payments, feedback</p>
                </div>

                <div className="bg-green-100 p-3 rounded border border-green-400">
                  <p className="font-semibold">Insurance Companies</p>
                  <p className="text-sm text-green-700">← claims, reports</p>
                  <p className="text-xs text-green-600">→ reimbursements</p>
                </div>

                <div className="bg-green-100 p-3 rounded border border-green-400">
                  <p className="font-semibold">Regulatory Bodies</p>
                  <p className="text-sm text-green-700">← compliance reports</p>
                </div>

                <div className="bg-yellow-100 p-3 rounded border border-yellow-400">
                  <p className="font-semibold">Waste Management</p>
                  <p className="text-sm text-gray-600">← medical waste</p>
                  <p className="text-sm text-gray-600">← general waste</p>
                </div>

                <div className="bg-green-100 p-3 rounded border border-green-400">
                  <p className="font-semibold">Community Health</p>
                  <p className="text-sm text-green-700">← preventive care</p>
                  <p className="text-sm text-green-700">← health education</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Competition Bar */}
        <div className="mt-6 bg-orange-200 p-4 rounded-lg border-2 border-orange-400">
          <h3 className="text-center font-bold text-lg">COMPETITION</h3>
          <p className="text-center text-sm">Other family clinics, urgent care centers, hospital outpatient departments, telehealth services</p>
          <p className="text-center text-xs mt-1">← competing for patients | → patient choice influences market share</p>
        </div>

        {/* Key Relationships Legend */}
        <div className="mt-6 bg-gray-100 p-4 rounded-lg border-2 border-gray-300">
          <h3 className="font-bold mb-2">Key Relationship Flows:</h3>
          <div className="grid grid-cols-2 gap-2 text-sm">
            <p>→ Primary flow direction</p>
            <p>↔ Bidirectional exchange</p>
            <p>← Return flow (payments, feedback)</p>
            <p>• Internal processes</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ClinicEnterpriseDiagram;