Energy Intensity Index (EII)
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:95" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=95" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Energy Intensity Index (EII) is a metric that compares the actual energy consumed during production to a theoretical or historical standard of energy consumption</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The primary objective of the EII is to identify energy efficiency levels within the production process</li><li>allowing for the detection of inefficiencies and opportunities for improvement</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The EII is calculated by dividing the actual energy consumed by the standard energy consumption, providing a ratio that indicates how energy usage compares to expected levels.</p>
               <div class="math-equation">$$ \mathit{EII} = \frac{\mathit{Actual\,Energy\,Consumed\,Gj}}{\mathit{Standard\,Energy\,Gj}} $$</div><ul><li>Actual Energy Consumed Gj: Value used in the calculation as defined by the code implementation.</li><li>Standard Energy Gj: Value used in the calculation as defined by the code implementation.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>The EII is utilized in key performance indicators related to energy management and operational efficiency</li><li>helping organizations monitor and optimize their energy consumption</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The inputs for calculating the EII include the actual energy consumed in gigajoules and the standard energy consumption in gigajoules</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>dimensionless</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The EII is typically reported from energy management systems or production monitoring systems that track energy usage and standards.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A value greater than 1.0 indicates that energy consumption is higher than the standard, signaling potential inefficiencies that may need to be addressed.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 5
   

      def calculate_energy_intensity_index(actual_energy_consumed_gj: float, standard_energy_gj: float) -> float:
       """Compares actual energy consumption to a theoretical or historical standard."""
       if standard_energy_gj == 0:
           return 1.0
       # KPI: Energy Intensity Index (EII)
       # A value > 1.0 indicates higher-than-standard energy consumption, signaling inefficiency.
       eii = actual_energy_consumed_gj / standard_energy_gj
       return eii

