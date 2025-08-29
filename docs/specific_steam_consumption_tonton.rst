Specific Steam Consumption (ton/ton)
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py:85" target="_blank" style="display: inline-block; background-color: #2c5282; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         VS Code
      </a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor&_Interactive_Bluebook_Generator/sample_project/petrochemical_plant_operations.py&line=85" target="_blank" style="display: inline-block; background-color: #000000; color: white; padding: 8px 12px; border-radius: 6px; text-decoration: none; font-weight: 500; font-size: 13px;">
         PyCharm
      </a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Specific Steam Consumption measures the amount of steam used in relation to the quantity of product produced</li><li>It is a critical indicator of energy efficiency within the production process</li><li>particularly in the separation and reaction stages</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of monitoring Specific Steam Consumption is to evaluate and improve the energy efficiency of the production process</li><li>ensuring that steam usage is optimized relative to the output of products</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The formula for Specific Steam Consumption is derived by dividing the total steam used in tons by the total product produced in tons. This provides a clear metric of steam consumption per unit of product.</p>
               <div class="math-equation">$$ \mathit{SSC} = \frac{\mathit{Steam\,Used\,Tons}}{\mathit{Product\,Produced\,Tons}} $$</div><ul><li>Steam Used Tons: Value used in the calculation as defined by the code implementation.</li><li>Product Produced Tons: Value used in the calculation as defined by the code implementation.</li></ul><script>if (window.MathJax) {  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }  else if (MathJax.typeset) { MathJax.typeset(); }}</script>
            </td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>Specific Steam Consumption is utilized in various Key Performance Indicators to assess energy efficiency and operational performance within the plant</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for calculating Specific Steam Consumption include the total amount of steam used in tons and the total amount of product produced in tons</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>ton/ton</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for Specific Steam Consumption is typically sourced from production logs and energy consumption records maintained within the plant's operational systems.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Monitoring Specific Steam Consumption can help identify areas for improvement in energy usage, potentially leading to cost savings and enhanced sustainability practices.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   .. code-block:: python
      :linenos:
   
      :emphasize-lines: 5
   

      def calculate_specific_steam_consumption(steam_used_tons: float, product_produced_tons: float) -> float:
       """Calculates how much steam is used per ton of product."""
       if product_produced_tons == 0:
           return 0.0
       # KPI: Specific Steam Consumption (ton/ton)
       # A primary indicator of energy efficiency in the separation and reaction sections.
       ssc = steam_used_tons / product_produced_tons
       return ssc