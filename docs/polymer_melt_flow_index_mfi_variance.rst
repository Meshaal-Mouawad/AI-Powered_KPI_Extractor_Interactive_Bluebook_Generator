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
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/abap_kpi.abap:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/abap_kpi.abap&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Polymer%20Melt%20Flow%20Index%20%28MFI%29%20Variance" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Polymer Melt Flow Index (MFI) Variance measures the variability in the flow characteristics of polymer materials</li><li>which is critical for assessing their processing behavior and end-use performance</li><li>The Polymer Melt Flow Index (MFI) Variance measures the variability in the melt flow index of polymer samples and indicates how easily the polymer flows when melted</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of monitoring MFI Variance is to ensure consistent polymer quality and performance by identifying deviations in flow properties that may affect manufacturing processes and product specifications</li><li>Monitoring MFI variance helps ensure consistent product quality and process stability</li><li>low variance suggests a stable process and adherence to quality standards</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The MFI Variance is calculated by determining the average of the squared differences between each individual MFI measurement and the overall mean MFI value, divided by the number of measurements.</p>
               <div class="math-equation">$$ \mathrm{MFI\ Variance} = \frac{\sum (x_i - \bar{x})^2}{n} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               49.7s (AI 49.7s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 49.657s
                  • AI: 49.657s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in quality control and process optimization metrics within polymer production and processing operations</li><li>Used in quality control and assurance to evaluate polymer production performance and detect potential manufacturing issues</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for calculating MFI Variance include individual MFI values obtained from testing polymer samples</li><li>Melt Flow Index test results from polymer samples collected during production or laboratory testing</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for MFI Variance is typically expressed in cubic centimeters per 10 minutes (cc/10 min), reflecting the flow rate of the polymer.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for MFI Variance is sourced from laboratory testing results and quality assurance reports generated during the polymer production process.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Monitoring MFI Variance is essential for maintaining product consistency and meeting industry standards, as significant variance may indicate issues in the polymerization process or raw material quality. Tracking MFI variance is essential for maintaining product quality and ensuring products meet required specifications for intended applications.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: abap
      :linenos:
   

      * KPI: Polymer Melt Flow Index (MFI) Variance
   * Formula: \mathrm{MFI\ Variance} = \frac{\sum (x_i - \bar{x})^2}{n}
   DATA: lv_var   TYPE f,
         gas_recovered_m3 TYPE f VALUE 120.0,
         total_gas_m3     TYPE f VALUE 450.0,
         lv_rate          TYPE f.

   lv_var = 0.0. " placeholder for variance example

   " Example KPI expression so the formula renders:
   lv_rate = ( gas_recovered_m3 / total_gas_m3 ) * 100.

   WRITE: / 'MFI Variance (example):', lv_var.
   WRITE: / 'Flare Gas Recovery Rate (%):', lv_rate.