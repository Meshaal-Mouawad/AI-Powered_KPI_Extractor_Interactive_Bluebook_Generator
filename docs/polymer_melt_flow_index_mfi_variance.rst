Polymer Melt Flow Index (MFI) Variance
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:180" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=180" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Polymer Melt Flow Index (MFI) Variance is a key performance indicator used to assess process efficiency and operational performance</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of Polymer Melt Flow Index (MFI) Variance is to provide a clear measure that supports monitoring</li><li>decision making</li><li>and continuous improvement</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>Calculated directly from the inputs found in the code implementation.</p>
               <div class="math-equation">$$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$</div><ul><li>Mfi Test Results: Value used in the calculation as defined by the code implementation.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI can serve as an input to higher-level operational and performance dashboards</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>Derived from the variables used in the code calculation for this KPI</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>See calculation and context for the most appropriate unit.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Typically sourced from process historians, production logs, or execution systems.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td></td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 5
   

      def calculate_polymer_mfi_variance(mfi_test_results: list) -> float:
       """Calculates the variance in Melt Flow Index, a key polymer quality metric."""
       if not mfi_test_results:
           return 0.0
       # KPI: Polymer Melt Flow Index (MFI) Variance
       # Low variance indicates consistent product quality and process stability.
       variance = np.var(mfi_test_results)
       return variance