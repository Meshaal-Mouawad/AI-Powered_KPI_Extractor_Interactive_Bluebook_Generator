Pump Vibration Anomaly Rate
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:135" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=135" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Pump Vibration Anomaly Rate measures the percentage of vibration readings from pumps that exceed a predefined safe threshold</li><li>This KPI is crucial for identifying potential issues in pump operation before they lead to failures</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The primary objective of this KPI is to facilitate predictive maintenance by monitoring pump vibrations</li><li>thereby allowing for timely interventions to prevent equipment failures</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The formula for calculating the Pump Vibration Anomaly Rate involves determining the ratio of the number of vibration readings that exceed the safe threshold to the total number of vibration readings, expressed as a percentage.</p>
               <div class="math-equation">$$ \mathit{Vibration\,Threshold} = \frac{\mathit{5.0\,#\,Mm}}{\mathit{S}} $$</div><ul><li>5.0 # Mm: Value used in the calculation as defined by the code implementation.</li><li>S: Value used in the calculation as defined by the code implementation.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in predictive maintenance strategies and reliability assessments for pump systems within industrial operations</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>Vibration readings from pumps</li><li>typically measured in millimeters per second</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>ratio (dimensionless)</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is sourced from vibration sensors installed on pumps, which continuously monitor and record vibration levels.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A high anomaly rate may indicate the need for maintenance or inspection of the pump, while a low rate suggests stable operation.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 7
   

      def calculate_pump_vibration_anomaly_rate(vibration_readings: list) -> float:
       """Calculates the percentage of vibration readings that exceed a safe threshold."""
       if not vibration_readings:
           return 0.0
       vibration_threshold = 5.0  # mm/s
       anomalies = [r for r in vibration_readings if r > vibration_threshold]
       # KPI: Pump Vibration Anomaly Rate
       # A predictive maintenance KPI used to anticipate pump failures and plan proactive maintenance.
       anomaly_rate = (len(anomalies) / len(vibration_readings)) * 100
       return anomaly_rate

