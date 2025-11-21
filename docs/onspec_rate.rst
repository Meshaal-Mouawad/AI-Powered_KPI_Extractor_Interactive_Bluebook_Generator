On-Spec Rate (%
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/sql_kpi.sql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/sql_kpi.sql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=On-Spec%20Rate%20%28%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The On-Spec Rate percentage measures the proportion of batches produced that meet the specified quality standards within a given timeframe</li><li>This KPI expresses the proportion of production that meets all quality standards relative to total batches</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>To ensure product quality and compliance with industry standards by maximizing the number of batches that are on-spec</li><li>Improve first-pass quality and reduce rework or off-spec material by monitoring on-spec performance over time</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The On-Spec Rate is calculated by dividing the number of on-spec batches by the total number of batches produced, then multiplying the result by 100 to express it as a percentage.</p>
               <div class="math-equation">$$ \mathrm{On\text{-}Spec\,\%} = \frac{\mathrm{On\text{-}Spec\,Batches}}{\mathrm{Total\,Batches}} \times 100 $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               1m 33s (AI 1m 33s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 92.537s
                  • AI: 92.536s
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
            <td><ul><li>This KPI is utilized in quality control assessments and performance evaluations to track production efficiency and product quality</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the count of on-spec batches and the total count of batches produced during the reporting period</li><li>Counts of on-spec batches and total batches in the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for the On-Spec Rate is a percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The data for this KPI is sourced from the batch quality summary, which aggregates quality metrics for all production batches.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher On-Spec Rate indicates better adherence to quality standards, which can lead to increased customer satisfaction and reduced costs associated with rework or non-compliance.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: On-Spec Rate (%)
   -- Formula: \mathrm{On\text{-}Spec\,\%} = \frac{\mathrm{On\text{-}Spec\,Batches}}{\mathrm{Total\,Batches}} \times 100
   CREATE VIEW kpi_on_spec_rate AS
   SELECT
       CAST(100.0 * on_spec_batches / NULLIF(total_batches, 0) AS FLOAT) AS on_spec_percentage
   FROM batch_quality_summary;